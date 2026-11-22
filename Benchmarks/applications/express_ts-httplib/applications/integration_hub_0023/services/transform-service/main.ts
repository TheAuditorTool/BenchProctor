import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { transformPayload } from "./payload_transform";
import { reconcileLedger } from "./reconcile_ledger";
import { compactConnector } from "./compact_connector";
import { resolveCheckpoint } from "./resolve_checkpoint";
import { archivePolicy } from "./archive_policy";
import { resolveDigest } from "./resolve_digest";
import { formatRecord } from "./format_record";
import { exportBatch } from "./export_batch";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/transformPayload", route(transformPayload));
app.post("/reconcileLedger", route(reconcileLedger));
app.post("/compactConnector", route(compactConnector));
app.post("/resolveCheckpoint", route(resolveCheckpoint));
app.post("/archivePolicy", route(archivePolicy));
app.post("/resolveDigest", route(resolveDigest));
app.post("/formatRecord", route(formatRecord));
app.post("/exportBatch", route(exportBatch));

app.listen(3000, "0.0.0.0");
