def direction(facing, turn):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    directions_count = len(directions)
    facing_index = directions.index(facing)
    steps = (turn // 45) % directions_count
    step_index = (facing_index + steps) % directions_count
    return directions[step_index]
