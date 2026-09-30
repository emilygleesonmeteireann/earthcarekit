from ._types import _BBoxSearch


def get_bbox_str(
    min_lat: str,
    min_lon: str,
    max_lat: str,
    max_lon: str,
):
    bounding_box = [min_lat, min_lon, max_lat, max_lon]
    return ",".join([str(float(x)) for x in bounding_box])


def parse_bbox_search(bounding_box: list[str | float | int] | None) -> _BBoxSearch:
    """Convert user's bounding box inputs to a query parameter, that can be used in search requests."""
    if bounding_box is not None:
        bbox = get_bbox_str(
            min_lat=str(float(bounding_box[0])),
            min_lon=str(float(bounding_box[1])),
            max_lat=str(float(bounding_box[2])),
            max_lon=str(float(bounding_box[3])),
        )
        return _BBoxSearch(bbox=bbox)
    return _BBoxSearch(bbox=None)
