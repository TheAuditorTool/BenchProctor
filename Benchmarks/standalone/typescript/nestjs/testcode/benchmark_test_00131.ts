// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, BadRequestException } from "@nestjs/common";
import { Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00131")
  async BenchmarkTest00131(): Promise<unknown> {
    const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const parts: string[] = [];
    for (const token of String(userInput).split(',')) { parts.push(token); }
    const data: string = parts.join(',');
    const _coerced = Math.max(0, Math.min(parseInt(String(data), 10) || 0, 1048576));
    const boundedVal = _coerced;
    const requested = boundedVal;
    if (!Number.isFinite(requested) || requested < 0 || requested > 1048576) { throw new BadRequestException({ error: "out of range" }); }
    const buf = Buffer.alloc(requested + 1);
    return { allocated: buf.length };
  }
}
