import { Router, Request, Response } from "express";

const router = Router();

router.get("/", (req: Request, res: Response): void => {
  const users = ["Raccoon", "Opossum", "Rat"];
  res.status(200).send(users);
});

export { router };
