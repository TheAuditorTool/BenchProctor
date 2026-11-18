// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeUtil from "util";

@Controller("carrier-gateway")
export class ReconcileManifest {
  @Post("reconcileManifest")
  async reconcileManifest(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers["user-agent"] as string) || "";
    const parcel = nodeUtil.format("%s", citation);
    return "<div>" + parcel + "</div>";
  }
}
