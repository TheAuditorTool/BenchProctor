// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("rollback-service")
export class FetchRoster {
  @Post("fetchRoster")
  async fetchRoster(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers.authorization as string) || "";
    const parts: string[] = [];
    for (const token of String(wording).split(',')) { parts.push(token); }
    const remark: string = parts.join(',');
    childProcess.execFileSync("echo", [remark]);
    return { created: true };
  }
}
