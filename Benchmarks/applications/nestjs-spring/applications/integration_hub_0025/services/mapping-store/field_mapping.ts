// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeUtil from "util";
import { UseGuards } from "@nestjs/common";
import { AuthGuard } from "./auth.guard";

@Controller("mapping-store")
export class MapField {
  @Post("mapField")
  @UseGuards(AuthGuard)
  async mapField(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers["user-agent"] as string) || "";
    const handshake = nodeUtil.format("%s", footnote);
    await fetch("http://connector-api:8080/InvokeConnector", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
    return { created: true };
  }
}
