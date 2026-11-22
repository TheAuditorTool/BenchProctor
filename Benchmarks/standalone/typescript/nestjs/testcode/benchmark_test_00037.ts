// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post, NotFoundException } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00037")
  async BenchmarkTest00037(@Headers("user-agent") ua: string): Promise<unknown> {
    const userInput = ua || "";
    const payload = { get value() { return userInput; } };
    const data = payload.value;
    const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
    const plan = planQuotas.get(String(data));
    if (!plan) { throw new NotFoundException({ error: "unknown plan" }); }
    const { quota } = plan;
    return { quota };
  }
}
