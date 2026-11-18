import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { openDispute } from "./dispute_open";
import { rotateMandate } from "./rotate_mandate";
import { resolveIndex } from "./resolve_index";
import { enrichWallet } from "./enrich_wallet";
import { auditReport } from "./audit_report";
import { mergeIndex } from "./merge_index";
import { compactCheckpoint } from "./compact_checkpoint";
import { archiveProfile } from "./archive_profile";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/openDispute", route(openDispute));
app.post("/rotateMandate", route(rotateMandate));
app.post("/resolveIndex", route(resolveIndex));
app.post("/enrichWallet", route(enrichWallet));
app.post("/auditReport", route(auditReport));
app.post("/mergeIndex", route(mergeIndex));
app.post("/compactCheckpoint", route(compactCheckpoint));
app.post("/archiveProfile", route(archiveProfile));

app.listen(3000, "0.0.0.0");
