import request from "supertest";

import app from "../../src/app";

describe("Garbage Friends routes", () => {
  test("Get all Garbage Friends", async () => {
    const res = await request(app).get("/garbage-friends");
    expect(res.body).toEqual(["Raccoon", "Opossum", "Rat"]);
  });
});
