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
  @Post("BenchmarkTest00221")
  async BenchmarkTest00221(): Promise<unknown> {
    const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    let data;
    try { data = JSON.parse(userInput).value || userInput; }
    catch (e) { data = userInput; }
    const _coerced = Math.max(0, Math.min(parseInt(String(data), 10) || 0, 1048576));
    const boundedVal = _coerced;
    const recordCount = boundedVal;
    if (!Number.isInteger(recordCount) || recordCount < 0 || recordCount > 16384) { throw new BadRequestException({ error: "too many records" }); }
    const table = new ArrayBuffer(recordCount * 64);
    return { allocated: table.byteLength };
  }
}
