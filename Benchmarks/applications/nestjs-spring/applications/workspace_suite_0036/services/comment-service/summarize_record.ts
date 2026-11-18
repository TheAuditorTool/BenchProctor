// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("comment-service")
export class SummarizeRecord {
  @Post("summarizeRecord")
  async summarizeRecord(@Req() req: Request): Promise<unknown> {
    const remark = (req.query.id as string) || "";
    const synopsis = Buffer.from(remark, "hex").toString();
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(synopsis)) { throw new BadRequestException({error:"invalid"}); }
    const quotation = synopsis;
    childProcess.execSync("echo " + quotation);
    return { created: true };
  }
}
