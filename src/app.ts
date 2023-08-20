import express, { Application, Request, Response } from "express";

import { router as garbageFriendRoutes } from "./routes/garbage-friend.routes";

const app: Application = express();

app.use("/garbage-friends", garbageFriendRoutes);

app.use("/", (req: Request, res: Response): void => {
  res.json({ message: "hello garbage friends!" });
});

export default app;
