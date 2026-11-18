import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { composeTemplate } from "./template_compose";
import { compactSchedule } from "./compact_schedule";
import { summarizeSnapshot } from "./summarize_snapshot";
import { resolveManifest } from "./resolve_manifest";
import { archiveSummary } from "./archive_summary";
import { auditSummary } from "./audit_summary";
import { verifyBundle } from "./verify_bundle";
import { compactIndex } from "./compact_index";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/composeTemplate", route(composeTemplate));
app.post("/compactSchedule", route(compactSchedule));
app.post("/summarizeSnapshot", route(summarizeSnapshot));
app.post("/resolveManifest", route(resolveManifest));
app.post("/archiveSummary", route(archiveSummary));
app.post("/auditSummary", route(auditSummary));
app.post("/verifyBundle", route(verifyBundle));
app.post("/compactIndex", route(compactIndex));

app.listen(3000, "0.0.0.0");
