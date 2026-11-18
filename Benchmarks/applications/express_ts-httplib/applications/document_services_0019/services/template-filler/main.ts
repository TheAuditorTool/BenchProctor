import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { fillTemplate } from "./template_fill";
import { verifyRoster } from "./verify_roster";
import { auditRecord } from "./audit_record";
import { compactLedger } from "./compact_ledger";
import { verifyBundle } from "./verify_bundle";
import { resolveProfile } from "./resolve_profile";
import { archiveBatch } from "./archive_batch";
import { annotateConfig } from "./annotate_config";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/fillTemplate", route(fillTemplate));
app.post("/verifyRoster", route(verifyRoster));
app.post("/auditRecord", route(auditRecord));
app.post("/compactLedger", route(compactLedger));
app.post("/verifyBundle", route(verifyBundle));
app.post("/resolveProfile", route(resolveProfile));
app.post("/archiveBatch", route(archiveBatch));
app.post("/annotateConfig", route(annotateConfig));

app.listen(3000, "0.0.0.0");
