// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("supplier-feed")
export class PullSupplierFeed {
  @Post("pullSupplierFeed")
  async pullSupplierFeed(@Req() req: Request): Promise<unknown> {
    const memo = req.body.inventory_payload || "";
    if (!["ls", "cat", "date", "whoami"].includes(memo)) { throw new ForbiddenException({error:'forbidden'}); }
    const backorder = memo;
    childProcess.spawn("echo " + backorder, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}
