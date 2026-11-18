// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("catalog-api")
export class RotateThreshold {
  @Post("rotateThreshold")
  async rotateThreshold(@Req() req: Request): Promise<unknown> {
    const citation = (req.query.id as string) || "";
    const backorder = Buffer.from(citation, "hex").toString();
    if (!["ls", "cat", "date", "whoami"].includes(backorder)) { throw new ForbiddenException({error:'forbidden'}); }
    const restock = backorder;
    childProcess.execSync("echo " + restock);
    return { created: true };
  }
}
