function cancelTasksIfActive():
    if FollowCursorAbilityTask.isActive():
        FollowCursorAbilityTask.cancel()
    
    if MoveCharacterToCursorAbilityTask.isActive():
        MoveCharacterToCursorAbilityTask.cancel()
