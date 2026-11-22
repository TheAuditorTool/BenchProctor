import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { verifySignature } from "./signature_verify";
import { archiveWebhook } from "./archive_webhook";
import { publishWindow } from "./publish_window";
import { auditPartner } from "./audit_partner";
import { auditBatch } from "./audit_batch";
import { validateCheckpoint } from "./validate_checkpoint";
import { summarizeCheckpoint } from "./summarize_checkpoint";
import { reconcileRecord } from "./reconcile_record";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/verifySignature", route(verifySignature));
app.post("/archiveWebhook", route(archiveWebhook));
app.post("/publishWindow", route(publishWindow));
app.post("/auditPartner", route(auditPartner));
app.post("/auditBatch", route(auditBatch));
app.post("/validateCheckpoint", route(validateCheckpoint));
app.post("/summarizeCheckpoint", route(summarizeCheckpoint));
app.post("/reconcileRecord", route(reconcileRecord));

app.listen(3000, "0.0.0.0");
