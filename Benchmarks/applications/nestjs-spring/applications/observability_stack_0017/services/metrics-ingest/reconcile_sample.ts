// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("metrics-ingest")
export class ReconcileSample {
  @Post("reconcileSample/:id")
  async reconcileSample(@Req() req: Request): Promise<unknown> {
    const note = (req.params.id as string) || "";
    const _raw = note;
    const cohort = (_raw && _raw.length > 0) ? _raw : 'default';
    return new StreamableFile(Buffer.from("<section>" + cohort + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
