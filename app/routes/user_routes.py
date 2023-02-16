from fastapi import APIRouter, Response, status
from app.config.db import users as collection
from app.schemas.user_schema import UserEntity, UsersEntity
from app.models.user_model import UserModel
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT

router = APIRouter()

@router.get('/', response_model=list[UserModel])
def fin_all_users():
    return UsersEntity(collection.find({}))

@router.post('/', response_model=UserModel)
def create_user(user: UserModel):
    new_user = dict(user)
    del new_user["id"]
    new_user["password"]=sha256_crypt.encrypt(new_user["password"])
    user_id = collection.insert_one(new_user).inserted_id
    user = collection.find_one({"_id": user_id})
    return UserEntity(user)

@router.get('/{id}', response_model=UserModel)
def fin_user(id:str): 
    return UserEntity(collection.find_one({"_id": ObjectId(id)})) 

@router.put('/{id}', status_code=status.HTTP_200_OK)
def put_user(id:str, user:UserModel):
    UserEntity(collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})) 
    return Response(status_code=HTTP_200_OK, content=f"User Updated")

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:str):
    UserEntity(collection.find_one_and_delete({"_id": ObjectId(id)})) 
    return Response(status_code=HTTP_204_NO_CONTENT)