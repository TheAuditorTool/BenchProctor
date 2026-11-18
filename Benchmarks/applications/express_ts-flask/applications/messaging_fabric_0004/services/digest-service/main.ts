import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { rollDigest } from "./digest_roll";
import { verifySchedule } from "./verify_schedule";
import { annotateProfile } from "./annotate_profile";
import { validateBatch } from "./validate_batch";
import { verifySubscription } from "./verify_subscription";
import { rotateDelivery } from "./rotate_delivery";
import { verifyPolicy } from "./verify_policy";
import { compactBatch } from "./compact_batch";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/rollDigest", route(rollDigest));
app.post("/verifySchedule", route(verifySchedule));
app.post("/annotateProfile", route(annotateProfile));
app.post("/validateBatch", route(validateBatch));
app.post("/verifySubscription/:id", route(verifySubscription));
app.post("/rotateDelivery", route(rotateDelivery));
app.post("/verifyPolicy", route(verifyPolicy));
app.post("/compactBatch/:id", route(compactBatch));

app.listen(3000, "0.0.0.0");
