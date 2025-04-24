# from sqlalchemy import Column, Integer, String, Text, DECIMAL, ForeignKey
# from sqlalchemy.orm import relationship
# from sqlalchemy import TIMESTAMP , func
# from database import Base
# import enum

# class User(Base):
#     __tablename__ = 'users'
#     userId = Column(Integer, primary_key=True, index=True)
#     username = Column(String(50), nullable=False)
#     email = Column(String(100), unique=True, nullable=False)
#     password = Column(String(255), nullable=False)
#     role = Column(String(30), nullable=False)

#     orders = relationship("Order", back_populates="user")

# class Game(Base):
#     __tablename__ = 'games'
#     gameId = Column(Integer, primary_key=True, index=True)
#     title = Column(String(100), nullable=False)
#     description = Column(Text)
#     price = Column(DECIMAL(10, 2), nullable=False)
#     genre = Column(String(30))
#     platform = Column(String(50))
#     created_at = Column(TIMESTAMP, server_default=func.now())
#     inventory = relationship("Inventory", back_populates="game", uselist=False)
#     order_items = relationship("OrderItem", back_populates="game")

# class Inventory(Base):
#     __tablename__ = 'inventory'
#     game_id = Column(Integer, ForeignKey("games.GameID"), primary_key=True)
#     stock_quantity = Column(Integer, nullable=False)

#     game = relationship("Game", back_populates="inventory")

# class Order(Base):
#     __tablename__ = 'orders'
#     id = Column("OrderID", Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.UserID"))
#     order_date = Column(DateTime, default=datetime.utcnow)
#     total_amount = Column(DECIMAL(10, 2))
#     status = Column(Enum(StatusEnum), default="pending")

#     user = relationship("User", back_populates="orders")
#     items = relationship("OrderItem", back_populates="order")
#     payment = relationship("Payment", back_populates="order", uselist=False)

# class OrderItem(Base):
#     __tablename__ = 'orderitems'
#     id = Column("OrderItemID", Integer, primary_key=True, index=True)
#     order_id = Column(Integer, ForeignKey("orders.OrderID"))
#     game_id = Column(Integer, ForeignKey("games.GameID"))
#     quantity = Column(Integer)
#     price = Column(DECIMAL(10, 2))

#     order = relationship("Order", back_populates="items")
#     game = relationship("Game", back_populates="order_items")

# class Payment(Base):
#     __tablename__ = 'payments'
#     id = Column("PaymentID", Integer, primary_key=True, index=True)
#     order_id = Column(Integer, ForeignKey("orders.OrderID"))
#     payment_date = Column(DateTime, default=datetime.utcnow)
#     payment_status = Column(Enum(PaymentStatusEnum), default="pending")
#     payment_method = Column(String(50))

#     order = relationship("Order", back_populates="payment")
