import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { pullSupplierFeed } from "./supplier_feed";
import { exportRecord } from "./export_record";
import { formatBundle } from "./format_bundle";
import { exportSnapshot } from "./export_snapshot";
import { publishCheckpoint } from "./publish_checkpoint";
import { publishDigest } from "./publish_digest";
import { reconcileBatch } from "./reconcile_batch";
import { compactCheckpoint } from "./compact_checkpoint";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/pullSupplierFeed", route(pullSupplierFeed));
app.post("/exportRecord", route(exportRecord));
app.post("/formatBundle", route(formatBundle));
app.post("/exportSnapshot", route(exportSnapshot));
app.post("/publishCheckpoint", route(publishCheckpoint));
app.post("/publishDigest", route(publishDigest));
app.post("/reconcileBatch", route(reconcileBatch));
app.post("/compactCheckpoint", route(compactCheckpoint));

app.listen(3000, "0.0.0.0");
