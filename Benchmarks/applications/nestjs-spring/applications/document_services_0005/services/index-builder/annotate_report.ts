// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("index-builder")
export class AnnotateReport {
  @Post("annotateReport")
  async annotateReport(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body?.payload as string) || "";
    const addendum = `${footnote}`;
    return new StreamableFile(Buffer.from("<section>" + addendum + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
