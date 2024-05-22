from fastapi import HTTPException, status


ObjectAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Объект с таким именем уже существует",
)


ObjectDoesNotExistException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Такого объекта не существует"
)
