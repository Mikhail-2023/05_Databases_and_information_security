#!/usr/bin/env python
# coding=utf-8
import pika

credentials = pika.PlainCredentials('vm1', '12')
parameters = pika.ConnectionParameters('192.168.0.151', 5672, 'host1', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello Netology!')
connection.close()
