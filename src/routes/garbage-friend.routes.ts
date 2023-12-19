import { Router, Request, Response } from "express";

const router = Router();
const animals = ["Raccoon", "Opossum", "Rat"];

router.get("/", (req: Request, res: Response): void => {
  res.status(200).send(animals);
});

export { router };
