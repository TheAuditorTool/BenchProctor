import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { schedulePayout } from "./payout_schedule";
import { rotateBundle } from "./rotate_bundle";
import { mergeMandate } from "./merge_mandate";
import { reconcileSchedule } from "./reconcile_schedule";
import { summarizeDigest } from "./summarize_digest";
import { exportManifest } from "./export_manifest";
import { publishConfig } from "./publish_config";
import { auditBundle } from "./audit_bundle";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/schedulePayout", route(schedulePayout));
app.post("/rotateBundle", route(rotateBundle));
app.post("/mergeMandate", route(mergeMandate));
app.post("/reconcileSchedule", route(reconcileSchedule));
app.post("/summarizeDigest", route(summarizeDigest));
app.post("/exportManifest", route(exportManifest));
app.post("/publishConfig", route(publishConfig));
app.post("/auditBundle", route(auditBundle));

app.listen(3000, "0.0.0.0");
