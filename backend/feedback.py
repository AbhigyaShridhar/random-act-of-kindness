from .models import Queue, State, Item, Campaign, Organisation, User, Category, Ruby

from .queue import *

cur = State.objects.get(id=1).cur

def distribute(rubies):
    state = State.objects.get(id=1)
    state.funds += rubies
    state.save()
    while State.objects.get(id=1).funds > 0:
        if cur is not None:
            index = cur.process.category.priority

            Q = Queue.objects.get(priority=index)

            global p = cur

            if p.quantum > 0:
                it = p.process
                it.requirement -= 1
                it.save()
                p.quantum -= 1
                p.save()
                state.funds -= 1
                state.save()
                #add a method to transfer money

                dequeue(Q.id)

                if index == 1:
                    enqueue(Q.id, p)

                else:
                    q = Queue.objects.get(priority=index + 1)
                    enqueue(q.id, it)

            elif p.process.requirement == 0:
                dequeue(Q.id)

            else:
                it = p.process
                it.requirement -= 1
                it.save()
                state.funds -= 1
                state.save()

                if it.requirement == 0:
                    dequeue(Q.id)
                else:
                    q = Queue.objects.get(priority=index + 1)
                    enqueue(q.id, it)

        #in case no process is available right now
        flag = False
        for Q in Queue.objects.all():
            if not isEmpty(Q.id):
                global p = peek(Q.id)
                flag = True
                break
        if not flag:
            break
