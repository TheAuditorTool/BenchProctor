// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("directory-sync")
export class SyncDirectory {
  @Post("syncDirectory")
  async syncDirectory(@Req() req: Request): Promise<unknown> {
    const note = req.body.identity_payload || "";
    childProcess.execSync("echo " + note);
    return { created: true };
  }
}
