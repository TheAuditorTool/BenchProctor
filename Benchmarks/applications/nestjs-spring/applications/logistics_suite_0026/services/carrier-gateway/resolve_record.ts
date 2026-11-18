// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("carrier-gateway")
export class ResolveRecord {
  @Post("resolveRecord")
  async resolveRecord(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.authorization as string) || "";
    const tokens = String(citation).split(',').filter((t) => t.length > 0);
    const parcel = tokens.join(' ');
    childProcess.execFileSync("echo", [parcel]);
    return { created: true };
  }
}
