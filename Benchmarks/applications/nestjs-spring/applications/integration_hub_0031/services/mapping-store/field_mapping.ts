// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("mapping-store")
export class MapField {
  @Post("mapField")
  async mapField(@Req() req: Request): Promise<unknown> {
    const snippet = (req.body as string) || "";
    const handshake = String(snippet).split(/[ \t]+/).join(" ");
    await fetch("http://connector-api:8080/InvokeConnector", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
    return { created: true };
  }
}
