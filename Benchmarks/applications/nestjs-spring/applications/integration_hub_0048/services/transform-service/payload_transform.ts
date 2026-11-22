// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("transform-service")
export class TransformPayload {
  @Post("transformPayload")
  async transformPayload(@Req() req: Request): Promise<unknown> {
    const citation = (await shared.mq.receive("app-events"));
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(citation);
    await fetch("http://partner-registry:8080/RegisterPartner", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
    return { created: true };
  }
}
