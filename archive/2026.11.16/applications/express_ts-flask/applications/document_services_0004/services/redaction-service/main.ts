import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { applyRedaction } from "./redaction_apply";
import { publishRoster } from "./publish_roster";
import { publishLedger } from "./publish_ledger";
import { enrichSnapshot } from "./enrich_snapshot";
import { annotateProfile } from "./annotate_profile";
import { publishSignature } from "./publish_signature";
import { reconcileAttachment } from "./reconcile_attachment";
import { summarizeCheckpoint } from "./summarize_checkpoint";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/applyRedaction", route(applyRedaction));
app.post("/publishRoster", route(publishRoster));
app.post("/publishLedger", route(publishLedger));
app.post("/enrichSnapshot", route(enrichSnapshot));
app.post("/annotateProfile", route(annotateProfile));
app.post("/publishSignature", route(publishSignature));
app.post("/reconcileAttachment", route(reconcileAttachment));
app.post("/summarizeCheckpoint", route(summarizeCheckpoint));

app.listen(3000, "0.0.0.0");
