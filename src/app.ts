import express, { Application, Request, Response, NextFunction } from "express";

import { router as garbageFriendRoutes } from "./routes/garbage-friend.routes";

const app: Application = express();

app.use("/garbage-friends", garbageFriendRoutes);

app.use("/", (req: Request, res: Response, next: NextFunction): void => {
  res.json({ message: "hello garbage friends!" });
});

export default app;
