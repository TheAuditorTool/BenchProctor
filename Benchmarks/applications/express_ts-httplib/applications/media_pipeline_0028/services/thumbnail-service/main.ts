import express, { Request, Response } from "express";
import session from "express-session";

import { renderThumbnail } from "./thumbnail_render";
import { mergeReceipt } from "./merge_receipt";
import { normalizeReceipt } from "./normalize_receipt";
import { collectPolicy } from "./collect_policy";
import { resolvePolicy } from "./resolve_policy";
import { collectRecord } from "./collect_record";
import { renderAsset } from "./render_asset";
import { pruneCheckpoint } from "./prune_checkpoint";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/renderThumbnail", renderThumbnail);
app.post("/mergeReceipt", mergeReceipt);
app.post("/normalizeReceipt", normalizeReceipt);
app.post("/collectPolicy", collectPolicy);
app.post("/resolvePolicy", resolvePolicy);
app.post("/collectRecord", collectRecord);
app.post("/renderAsset", renderAsset);
app.post("/pruneCheckpoint", pruneCheckpoint);

app.listen(3000, "0.0.0.0");
