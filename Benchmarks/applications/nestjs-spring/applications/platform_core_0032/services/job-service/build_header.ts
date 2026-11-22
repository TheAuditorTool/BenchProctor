// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("job-service")
export class BuildHeader {
  @Post("buildHeader")
  async buildHeader(@Req() req: Request): Promise<unknown> {
    const remark = (req.query.id as string) || "";
    const [persona] = String(remark).split(',');
    return new StreamableFile(Buffer.from("<section>" + persona + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
