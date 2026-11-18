// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("customs-service")
export class ReconcileProfile {
  @Post("reconcileProfile")
  async reconcileProfile(@Req() req: Request): Promise<unknown> {
    const phrase = (req.query.id as string) || "";
    const parcel = Buffer.from(phrase, "hex").toString();
    if (!["ls", "cat", "date", "whoami"].includes(parcel)) { throw new ForbiddenException({error:'forbidden'}); }
    const consignment = parcel;
    childProcess.execSync("echo " + consignment);
    return { created: true };
  }
}
