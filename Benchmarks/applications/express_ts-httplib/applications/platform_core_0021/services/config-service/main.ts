import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { rolloutConfig } from "./config_rollout";
import { archiveRoster } from "./archive_roster";
import { renderQuota } from "./render_quota";
import { mergePolicy } from "./merge_policy";
import { archiveConfig } from "./archive_config";
import { rotateBundle } from "./rotate_bundle";
import { auditHeader } from "./audit_header";
import { verifyReceipt } from "./verify_receipt";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/rolloutConfig", route(rolloutConfig));
app.post("/archiveRoster", route(archiveRoster));
app.post("/renderQuota", route(renderQuota));
app.post("/mergePolicy", route(mergePolicy));
app.post("/archiveConfig", route(archiveConfig));
app.post("/rotateBundle", route(rotateBundle));
app.post("/auditHeader", route(auditHeader));
app.post("/verifyReceipt", route(verifyReceipt));

app.listen(3000, "0.0.0.0");
