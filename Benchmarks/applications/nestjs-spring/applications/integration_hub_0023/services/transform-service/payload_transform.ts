// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("transform-service")
export class TransformPayload {
  @Post("transformPayload")
  async transformPayload(@Req() req: Request): Promise<unknown> {
    const caption = (req.query.id as string) || "";
    const [handshake] = String(caption).split(',');
    await fetch("http://connector-api:8080/InvokeConnector", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
    return { created: true };
  }
}
