from .models import Queue, Item

def isEmpty(id):
    queue = Queue.objects.get(id=id)
    if Item.objects.filter(queue=queue).exists():
        return False

    return True

def size(id):
    queue = Queue.objects.get(id=id)
    return Item.objects.filter(queue=queue).count()

def peek(id):
    queue = Queue.objects.get(id=id)
    item = Item.objects.get(queue=queue, id=1)
    return item

def enqueue(id, campaign):
    queue = Queue.objects.get(id=id)
    item = Item.objects.create(process=campaign, queue=queue)
    return

def dequeue(id):
    queue = Queue.objects.get(id=id)
    item = Item.objects.get(queue=queue, id=1)
    campaign = item.process
    item.delete()
    items = Item.objects.filter(queue=queue)
    for i in items:
        i.id = i.id - 1
    return campaign
