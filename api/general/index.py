from fastapi import APIRouter

router = APIRouter(
    tags=["general"],
)


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/ready")
def ready():
    return {"status": "ok"}
