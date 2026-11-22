// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("bounce-handler")
export class RecordBounce {
  @Post("recordBounce")
  async recordBounce(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers.origin as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(preface);
    const bulletin: string = readInput();
    await fetch("http://delivery-service:8080/DispatchDelivery", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
    return { created: true };
  }
}
