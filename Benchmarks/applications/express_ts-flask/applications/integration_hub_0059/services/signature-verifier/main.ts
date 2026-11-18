import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { verifySignature } from "./signature_verify";
import { reconcileWebhook } from "./reconcile_webhook";
import { validateProfile } from "./validate_profile";
import { enrichMapping } from "./enrich_mapping";
import { collectManifest } from "./collect_manifest";
import { collectCheckpoint } from "./collect_checkpoint";
import { auditRoster } from "./audit_roster";
import { exportDigest } from "./export_digest";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/verifySignature", route(verifySignature));
app.post("/reconcileWebhook", route(reconcileWebhook));
app.post("/validateProfile", route(validateProfile));
app.post("/enrichMapping", route(enrichMapping));
app.post("/collectManifest", route(collectManifest));
app.post("/collectCheckpoint", route(collectCheckpoint));
app.post("/auditRoster", route(auditRoster));
app.post("/exportDigest", route(exportDigest));

app.listen(3000, "0.0.0.0");
