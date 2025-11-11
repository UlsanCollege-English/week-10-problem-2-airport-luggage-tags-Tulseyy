"""
HW02 — Airport Luggage Tags (Open Addressing with Delete)
Implement linear probing with EMPTY and DELETED markers.
"""

# Step 4: create unique marker objects
EMPTY = object()
DELETED = object()

def make_table_open(m):
    """Return a table of length m filled with EMPTY markers."""
    # Step 4–6: Create table with EMPTY markers
    return [(EMPTY, None) for _ in range(m)]

def _find_slot_for_insert(t, key):
    """Return index to insert/overwrite (may return DELETED slot). Return None if full."""
    # Step 4–6: probe with wrap; remember first DELETED
    m = len(t)
    h = hash(key) % m
    first_deleted = None
    
    for i in range(m):
        idx = (h + i) % m
        marker, _ = t[idx]
        
        # Found exact key match - return to overwrite
        if marker != EMPTY and marker != DELETED and marker == key:
            return idx
        
        # Found DELETED slot - remember first one
        if marker is DELETED and first_deleted is None:
            first_deleted = idx
        
        # Found EMPTY slot
        if marker is EMPTY:
            # If we found a DELETED slot earlier, use it
            if first_deleted is not None:
                return first_deleted
            # Otherwise use this EMPTY slot
            return idx
    
    # Table is full - return first DELETED if we found one
    return first_deleted

def _find_slot_for_search(t, key):
    """Return index where key is found; else None. DELETED does not stop search."""
    # Step 4–6: Search for key, skip DELETED slots
    m = len(t)
    h = hash(key) % m
    
    for i in range(m):
        idx = (h + i) % m
        marker, _ = t[idx]
        
        # Found the key
        if marker == key:
            return idx
        
        # Found EMPTY - key not in table
        if marker is EMPTY:
            return None
        
        # DELETED does not stop search - continue probing
    
    # Probed entire table without finding key
    return None

def put_open(t, key, value):
    """Insert or overwrite (key, value). Return True on success, False if table is full."""
    # Step 5–6: use _find_slot_for_insert; handle overwrite
    idx = _find_slot_for_insert(t, key)
    
    if idx is None:
        # Table is full
        return False
    
    # Insert or overwrite at found position
    t[idx] = (key, value)
    return True

def get_open(t, key):
    """Return value for key or None if not present."""
    # Step 5–6: use _find_slot_for_search
    idx = _find_slot_for_search(t, key)
    
    if idx is None:
        return None
    
    _, value = t[idx]
    return value

def delete_open(t, key):
    """Delete key if present. Return True if removed, else False."""
    # Step 5–6: mark slot as DELETED
    idx = _find_slot_for_search(t, key)
    
    if idx is None:
        return False
    
    # Mark as DELETED
    t[idx] = (DELETED, None)
    return True

if __name__ == "__main__":
    # Optional manual checks (not graded)
    pass
