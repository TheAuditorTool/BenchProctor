import express, { Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { postComment } from "./comment_post";
import { reconcileManifest } from "./reconcile_manifest";
import { reconcileComment } from "./reconcile_comment";
import { compactManifest } from "./compact_manifest";
import { loadReceipt } from "./load_receipt";
import { annotateLedger } from "./annotate_ledger";
import { archiveSnapshot } from "./archive_snapshot";
import { formatRecord } from "./format_record";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/postComment", postComment);
app.post("/reconcileManifest/:id", reconcileManifest);
app.post("/reconcileComment", reconcileComment);
app.post("/compactManifest", compactManifest);
app.post("/loadReceipt", loadReceipt);
app.post("/annotateLedger", annotateLedger);
app.post("/archiveSnapshot", archiveSnapshot);
app.post("/formatRecord", formatRecord);

app.listen(3000, "0.0.0.0");
