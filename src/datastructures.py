
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name
        self._next_id = 1
        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generate_id = self._next_id
        self._next_id += 1
        return generate_id

    def add_member(self, member: dict):
        if isinstance(member, dict):
            self._members.append(member)
        else:
            return "Nada"

        return member
        # fill this method and update the return

    def delete_member(self, id):
        # fill this method and update the return
        for i, member in enumerate(self._members):
            if member["id"] == id:
                remove_member = self._members.pop(i)
                return remove_member
        return None
        
        pass

    def get_member(self, id):
        member = next((m for m in self._members if m["id"] == id), None)
        if member:
            if isinstance(member.get("lucky_numbers"), set):
                member["lucky_numbers"] = list(member["lucky_numbers"])
            return member
        return None

        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
