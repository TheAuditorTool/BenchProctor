// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("platform-api")
export class FetchBatch {
  @Post("fetchBatch")
  async fetchBatch(@Req() req: Request): Promise<unknown> {
    const note = (req.headers["x-custom-header"] as string) || "";
    const [handshake] = String(note).split(',');
    if (!["ls", "cat", "date", "whoami"].includes(handshake)) { throw new ForbiddenException({error:'forbidden'}); }
    const persona = handshake;
    childProcess.execSync("echo " + persona);
    return { created: true };
  }
}
