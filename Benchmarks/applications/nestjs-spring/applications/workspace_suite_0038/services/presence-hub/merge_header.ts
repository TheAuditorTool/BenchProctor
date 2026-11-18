// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("presence-hub")
export class MergeHeader {
  @Post("mergeHeader")
  async mergeHeader(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers.authorization as string) || "";
    const tokens = String(preface).split(',').filter((t) => t.length > 0);
    const remark = tokens.join(' ');
    childProcess.execFileSync("echo", [remark]);
    return { created: true };
  }
}
