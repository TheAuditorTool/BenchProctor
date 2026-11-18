// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post } from "@nestjs/common";
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
  @Post("BenchmarkTest00707")
  async BenchmarkTest00707(@Body("variables") vars: { input?: string }): Promise<unknown> {
    const userInput = (vars?.input as string) || "";
    const payload = { get value() { return userInput; } };
    const data = payload.value;
    const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
    const value = (row as any).name;
    return { created: true };
  }
}
