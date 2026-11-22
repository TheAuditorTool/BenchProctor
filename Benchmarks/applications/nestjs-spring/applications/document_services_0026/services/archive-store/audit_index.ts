// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("archive-store")
export class AuditIndex {
  @Post("auditIndex")
  async auditIndex(@Req() req: Request): Promise<unknown> {
    const preface = (req.body?.payload as string) || "";
    const addendum = `${preface}`;
    return new StreamableFile(Buffer.from("<section>" + addendum + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
