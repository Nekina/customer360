from django.shortcuts import render
from datetime import date, timedelta
from django.db.models import Count
from .models import *

def index(request): # Home
    customers = Customer.objects.all()
    context = { "customers": customers }
    return render(request, "index.html", context=context)

def create_customer(request): # New Customer
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        social_media = request.POST["social_media"]
        customer = Customer.objects.create(
            name = name,
            email = email,
            phone = phone,
            address = address,
            social_media = social_media
        )
        msg = f"Successfully saved new customer {name}"
        return render(request, "add.html", context={"msg":msg})
    return render(request, "add.html")

def summary(request): # Summary
    thirty_days_ago = date.today() - timedelta(days=30)
    interactions = Interaction.objects.filter(interaction_date__gte=thirty_days_ago)
    count = len(interactions)
    grouped_interactions = (
        interactions
        .values("channel", "direction") # group queryset by channel and direction
        .annotate(count=Count("channel")) # add count field
    )
    context = { "interactions":grouped_interactions, "count":count }
    return render(request, "summary.html", context=context)

def interact(request,cid):
    if request.method == "GET":
        channels = Interaction.CHANNEL_CHOICES
        directions = Interaction.DIRECTION_CHOICES
        context = {"channels":channels,"directions":directions}
        return render(request, "interact.html", context=context)

    if request.method == "POST":
        customer = Customer.objects.get(id=cid)
        channel = request.POST["channel"]
        direction = request.POST["direction"]
        summary = request.POST["summary"]
        interaction = Interaction.objects.create(
            customer = customer,
            channel = channel,
            direction = direction,
            summary = summary
        )
        context = { "msg": "Interaction Success" }
        return render(request, "interact.html", context=context)
